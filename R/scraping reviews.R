# Google Play Store review crawling
# Uber drive

install.packages("RSelenium")
install.packages("rvest")
install.packages("stringr")

library(RSelenium)
library(rvest)
library(strigr)

setwd("C:\\Users\\Desktop\\please")

remDr <- remoteDriver(remoteServerAddr="localhost", port=4445L, browserName="chrome")
remDr$open()
remDr$navigate("https://play.google.com/store/apps/details?id=com.dki.spb_android&showAllReviews=true")

webElem <- remDr$findElement("css", "body")
webElem$sendKeysToElement(list(key = "end"))

flag <- TRUE
endCnt <- 0

while (flag) {
  Sys.sleep(10)
  webElemButton <- remDr$findElements(using = 'css selector',value = '.ZFr60d.CeoRYc')
  
  if(length(webElemButton)==1){
    endCnt <- 0
    webElem$sendKeysToElement(list(key = "home"))
    webElemButton <- remDr$findElements(using = 'css selector',value = '.ZFr60d.CeoRYc')
    remDr$mouseMoveToLocation(webElement = webElemButton[[1]])
    remDr$click()
    webElem$sendKeysToElement(list(key = "end"))
    flag <- FALSE 
  }else{
    if(endCnt>3){
      flag <- FALSE
    }else{
      endCnt <- endCnt + 1
    }
  }
}


frontPage <- remDr$getPageSource()
reviewNames <- read_html(frontPage[[1]]) %>% html_nodes('.bAhLNe.kx8XBd') %>% html_nodes('.X43Kjb') %>%  html_text() 
reviewHelpful<- read_html(frontPage[[1]]) %>% html_nodes('.YCMBp.GVFJbb') %>% html_nodes('.jUL89d.y92BAb') %>% html_text() 
reviewComments <- read_html(frontPage[[1]]) %>% html_nodes('.UD7Dzf') %>%  html_text()
reviewStars <- read_html(frontPage[[1]]) %>% html_nodes('.nt2C1d') %>% html_nodes('.pf5lIe') %>% html_children() %>% html_attr("aria-label")
reviewData <- data.frame(name=reviewNames, stars=reviewStars, helpful=reviewHelpful, comment=reviewComments)


write.csv(reviewData, paste0("review_data(",nrow(reviewData),").csv"))

remDr$close()
