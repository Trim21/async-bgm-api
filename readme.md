# Async Bgm.tv API Client

[![Build Status](https://dev.azure.com/trim21/async-bgm-api/_apis/build/status/Trim21.async-bgm-api?branchName=master)](https://dev.azure.com/trim21/async-bgm-api/_build/latest?definitionId=4&branchName=master)
[![](https://img.shields.io/pypi/v/async-bgm-api.svg)](https://pypi.python.org/pypi/async-bgm-api)
[![](https://img.shields.io/codecov/c/github/Trim21/async-bgm-api/master.svg)](https://codecov.io/gh/Trim21/async-bgm-api)
[![](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/Trim21/async-bgm-api/blob/master/LICENSE)

```bash
pip install async_bgm_api
```

```python
import asyncio
from async_bgm_api import BgmApi

mirror_client = BgmApi(mirror=True)
client = BgmApi()


async def main():
    user = await mirror_client.get_user_info("trim21")
    print(user.nickname)

    calendar = await mirror_client.get_calendar()
    print(len(calendar))

    # mirror_client.get_subject_small
    # mirror_client.get_subject_media
    subject = await mirror_client.get_subject_large(8)
    print(subject.name_cn)
    print(subject.summary)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
```
