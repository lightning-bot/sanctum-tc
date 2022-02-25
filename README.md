# Sanctum-TC

Library for interacting with the Sanctum API


## Usage

```py
import asyncio

from sanctum import HTTPClient

async def main():
    client = HTTPClient("<your-api-url>", "<your-api-key>")
    resp = await client.get_guild(527887739178188830)
    print(resp)
    await client.close()

asyncio.run(main())
```