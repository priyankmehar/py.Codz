getwd()
setwd("D:/PGPBABI/Capstone")

TRANSACTION = read.csv(file.choose())

str(TRANSACTION)
summary(TRANSACTION)
top_TRANSACTION=head(TRANSACTION,100)
TRANSACTION_STR <- read.csv(file.choose(),header = T,
                               colClasses = c(rep("factor", 3),rep("character",1),
                                              rep("factor", 1),rep("numeric",1),
                                              rep("character", 1),rep("numeric",1),
                                              rep("factor", 4)),
                               na.strings=c("NA","NaN", " "))
#View(TRANSACTION_TICKET)
#summary(TRANSACTION_TICKET)


SR_TRAN = transform(TRANSACTION, ClientID=as.numeric(factor(ClientID)))
write.csv(SR_TRAN, file = "TRIM_SourceXn.csv")

head(SR_TRAN)

TRANSACTION_TICKET
iTT = 1
naListTT = c()
# noNAsTT = c()
# namesTT = c()
for(iTT in 1:length(TRANSACTION_TICKET))
{
  # namesTT = c(namesTT, names(TRANSACTION_TICKET[iTT]))
  # noNAsTT = c(noNAsTT,as.numeric(sum(is.na(TRANSACTION_TICKET[iTT]))))
  if(sum(is.na(TRANSACTION_TICKET[iTT]))/nrow(TRANSACTION_TICKET[iTT]) > 0.5)
  {
    naListTT = c(naListTT,iTT)
  }
}