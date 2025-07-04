import asyncio

from pyppeteer import launch

from . import catalog


async def main():
    html = catalog.render("Layout", cards=[x for x in range(69)])

    browser = await launch()
    page = await browser.newPage()
    await page.setViewport({"width": 4096, "height": 4096, "deviceScaleFactor": 1})
    await page.setContent(html)
    await page.screenshot({'path': 'output.png'})
    await browser.close()


asyncio.run(main())
print("Job's done.")