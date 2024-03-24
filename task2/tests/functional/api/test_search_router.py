import pytest
from httpx import AsyncClient


@pytest.mark.asyncio(scope="class")
class TestSearchRouter:
    BASE_URL = "/api/search"

    async def test_get_target_id_path(self, async_client: AsyncClient, target_id_path_cases):
        for case in target_id_path_cases:
            target_id = case["target_id"]
            result = case["result"]
            response = await async_client.get(
                self.BASE_URL + "/get_path",
                params={"target_id": target_id}
            )
            assert response.status_code == result["code"]
            assert response.json() == result["body"]
