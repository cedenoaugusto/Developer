import os
import msj_proactivos as principal
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='C:/Users/Augusto/AcondaSodimac/connections/sa-desarrollo-local-augusto.json'

# unit test
# resultado = principal.procesar_envio()

import urllib

import google.auth.transport.requests
import google.oauth2.id_token

def make_authorized_get_request(service_url='https://southamerica-east1-sod-cl-bi-sandbox.cloudfunctions.net/cf_crm_wa_msj_proactivos'):
    """
    make_authorized_get_request makes a GET request to the specified HTTP endpoint
    in service_url (must be a complete URL) by authenticating with the
    ID token obtained from the google-auth client library.
    """

    req = urllib.request.Request(service_url)

    auth_req = google.auth.transport.requests.Request()
    id_token = google.oauth2.id_token.fetch_id_token(auth_req, service_url)

    req.add_header("Authorization", f"Bearer {id_token}")
    response = urllib.request.urlopen(req)

    print(response.read())


make_authorized_get_request()


