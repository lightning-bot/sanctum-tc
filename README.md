# Sanctum-TC

Library for interacting with the Sanctum API


## Usage

```py
from sanctum import HTTPClient

client = HTTPClient("<your-api-url>", "<your-api-key")

async def main():
    resp = await client.get_guild(527887739178188830)
    print(resp)

asyncio.run(main())
```