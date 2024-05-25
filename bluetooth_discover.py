'''
from https://github.com/hbldh/bleak readme
use this script to find the mac address of your arduino (identified by the local name)
'''

import asyncio
from bleak import BleakScanner

async def main():
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)

if __name__ == "__main__":
    asyncio.run(main()) # for standard users
    # await main() # for Jupyter/IPython user
