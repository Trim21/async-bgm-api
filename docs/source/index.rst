================================
Asyncio Bgm.tv api client
================================

安装
========

.. code-block::

    pip install async_bgm_api

使用
========

.. code-block:: python

    from async_bgm_api import BgmApi

    mirror_client = BgmApi(mirror=True)

    async def main():
        user = await mirror_client.get_user_info("trim21")

.. toctree::

    api
