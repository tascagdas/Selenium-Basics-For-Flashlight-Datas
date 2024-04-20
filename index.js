const {By, Builder, Browser, Key} = require('selenium-webdriver');
const {delayed} = require("selenium-webdriver/lib/promise");

async function firstTest() {
    let driver;

    driver = await new Builder().forBrowser(Browser.CHROME).build();



    await driver.get("https://www.olight.com")

    await driver.manage().window().maximize();

    await driver.findElement(By.xpath("/html/body/div/main/div/div[2]/div/div[1]/div/div[1]/div[1]/a")).click();


    for (let i = 0; i < 5; i++) {

        await driver.executeScript("window.scrollTo(0, document.body.scrollHeight)");

        await delayed(1000);
    }

    var products = await driver.findElements(By.className("product-item-box"));

    for (let p = 0; p < products.length; p++) {
        let productLink = await products[p].findElement(By.className('link-box')).getAttribute('href');



        await driver.get(productLink)


        await driver.findElement(By.xpath("/html/body/div/main/div/div[2]/div/div[1]/div[2]/section[3]/div/div/div[2]/div/span")).click();


        let specCard=await driver.findElements(By.className("attributes-item-child"))
        for (let j = 0; j < specCard.length; j++) {
            const specKey = await specCard[j].findElement(By.className("attributes-item-name")).getText();
            const specValue = await specCard[j].findElement(By.className("attributes-item-value")).getText();
            await console.log(specKey, specValue);

        }
    }


    setTimeout(async () => {
        await driver.quit();
    }, 5000)

}


firstTest();
