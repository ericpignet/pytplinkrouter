"""Run TPLink from the command-line."""
import sys
from pytplinkrouter import TPLinkRouterFactory


def main():
    """Scan for devices and print results."""
    factory = TPLinkRouterFactory(*sys.argv[1:])
    router = factory.get_router()
    devices = router.scan_devices()

    if devices is None:
        print("Error communicating with the Netgear router")

    else:
        for i in devices:
            print(i)

if __name__ == '__main__':
    main()
