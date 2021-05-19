from main.libs.memcache import Client, memcache_client


def test_memcache(mocker):
    mock_set_function_param = []

    def mock_set(**__):
        mock_set_function_param.append(0)

    mocker.patch.object(Client, "get", return_value=0)
    mocker.patch.object(Client, "set", side_effect=mock_set)

    assert memcache_client.get("key") == 0
    memcache_client.set("key", 2)
    assert mock_set_function_param == [0]
