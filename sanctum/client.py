import aiohttp

__all__ = ("HTTPClient", )


class HTTPClient:
    def __init__(self, api_url: str, token: str) -> None:
        self.api_url = api_url
        self.session = aiohttp.ClientSession(headers={"User-Agent": "Sanctum-TC (https://gitlab.com/lightning-bot/sanctum-tc.git)",
                                                      "Authorization": f"Bearer {token}"})

    async def request(self, method: str, path: str, **kwargs):
        """Makes a request to the api.

        Parameters
        ----------
        method : str
            The method to use to send a request to the route. GET, PUT, POST, DELETE
        path : str
            The path to send the request to.
        """
        url = self.api_url + path
        resp = await self.session.request(method, url, **kwargs)
        return await resp.json()

    async def get_guild(self, guild_id: int):
        return await self.request("GET", f"/guilds/{guild_id}")

    async def create_guild(self, guild_id: int, payload: dict):
        return await self.request("PUT", f"/guilds/{guild_id}/create", data=payload)

    async def update_guild(self, guild_id: int, payload: dict):
        return await self.create_guild(guild_id, payload)