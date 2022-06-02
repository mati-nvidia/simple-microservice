import omni.ext
from omni.services.core import main
import omni.usd


def ping():
    return "pong"


class SimpleMicroserviceExtension(omni.ext.IExt):
    def on_startup(self, ext_id):
        print("[maticodes.services.simple] SimpleMicroserviceExtension startup")
        main.register_endpoint("get", "/ping", ping, tags=["Simple Service"])

    def on_shutdown(self):
        print("[maticodes.services.simple] SimpleMicroserviceExtension shutdown")
        main.deregister_endpoint("get", "/ping")
