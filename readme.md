# Async Bgm.tv API Client

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
