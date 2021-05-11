print("jello")
#array of each beer type with their flavor profile *as of 5/8/2021*
americanWildAle = [""]
barleywine = [""]
belgianBlonde = [""]
belgianDubbel = ["spicy", "malty", "caramel", "yeasty"]
belgianQuadrupel = [""]
belgianStrongGoldenAle = [""]
bièreDeChampagne = [""]
bièreBrut = [""]
blondeAle = [""]
bock = ["creamy", "malty", "bittersweet", "cocoa"]
blondeAle = [""]
brownAle = [""]
californiaCommon = [""]
chilli = [""]
cider = [""]
creamAle = [""]
doppelbock = ["caramel", "malty", "roasted"]
dunkelweizen = [""]
englishBitter = ["hoppy", "malty", "nutty", "woody", "spicy"]
englishOld = ["sweet", "fruity", "raisin", "caramel", "hoppy"]
extraSpecial = [""]
farmhouseAle = [""]
freeze = [""]
fruitBeer = [""]
gingerBeer = ["spicy", "ginger", "tart"]
goldenAle = ["malty", "spicy", "hoppy"]
grapeAle = [""]
grisette = [""]
gruit = [""]
hefeweizen = [""]
honeyBeer = [""]
ipa = ["piney", "hoppy", "resin"]
kellerbier = [""]
kölsch = [""]
kristallweizen = [""]
kvass = [""]
lager = [""]
lambic = ["tart", "fruity", "sour"]
lichtenhainer = [""]
märzen = [""]
mead = ["honey", "semi-sweet"]
oatmealStout = ["creamy", "roasted", "malty", "caramel"]
paleAle = [""]
pilsner = ["sweet", "malty", "caramel", "spice"]
porter = ["roasted", "malty", "chocolate"]
redAle = [""]
saison = ["creamy", "malty", "citrus", "tart"]
schwarzbier = ["bittersweet", "malty"]
scotchAle = ["caramel", "toffee", "roasted", "malty"]
shandy = [""]
smokedBeer = [""]
sour = [""]
spicedBeer = [""]
stout = ["roasted", "malty", "caramel", "hoppy"]
strongAle = [""]
traditionalAle = [""]
pumpkinBeer = [""]
wheatBeer = [""]
wildAle = [""]
winterAle = [""]

#array of all beer types. use camelCase for any new
flavors = [americanWildAle, barleywine, belgianBlonde, belgianDubbel, belgianQuadrupel, belgianStrongGoldenAle, bièreDeChampagne, bièreBrut, blondeAle, bock, brownAle, 
californiaCommon, chilli, cider, creamAle, doppelbock, dunkelweizen, englishBitter, englishOld, extraSpecial, farmhouseAle, freeze, fruitBeer, gingerBeer, goldenAle, 
grapeAle, grisette, gruit, hefeweizen, honeyBeer, ipa, kellerbier, kölsch, kristallweizen, kvass, lager, lambic, lichtenhainer, märzen, 
mead, oatmealStout, paleAle, pilsner, porter,  redAle, saison, schwarzbier, scotchAle, shandy, smokedBeer, sour, spicedBeer, stout, strongAle, traditionalAle, pumpkinBeer, 
wheatBeer, wildAle, winterAle]



#create CSV of the flavors array
import csv
with open("flavors.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(flavors)

