print("jello")
#array of all beer types. use camelCase for any new
flavors = [americanWildAle, barleywine, belgianBlonde, belgianDubbel, belgianQuadrupel, belgianStrongGoldenAle, bièreDeChampagne, bièreBrut, blondeAle, Bock, brownAle, 
californiaCommon, chilli, cider, creamAle, doppelbock, dunkelweizen, englishBitter, englishOld, strongAle, extraSpecial, farmhouseAle, freeze, fruitBeer, gingerBeer, gluten, 
goldenAle, grapeAle, grisette, gruit, hefeweizen, honeyBeer, ipa, kellerbier, kölsch, kristallweizen, kvass, lager, lambic, lichtenhainer, märzen, 
mead, oatmealStout, paleAle, pilsner, porter,  redAle, saison, schwarzbier, scotchAle, shandy, smokedBeer, sour, spicedBeer, stout, strongAle, traditionalAle, pumpkinBeer, 
wheatBeer, wildAle, winterAle]

#array of each beer type with their flavor profile *as of 5/8/2021*
belgianDubbel = ["spicy", "malty", "caramel", "yeasty"]
bock = ["creamy", "malty", "bittersweet", "cocoa"]
doppelbock = ["caramel", "malty", "roasted"]
englishBitter = ["hoppy", "malty", "nutty", "woody", "spicy"]
englishOld = ["sweet", "fruity", "raisin", "caramel", "hoppy"]
gingerBeer = ["spicy", "ginger", "tart"]
goldenAle = ["malty", "spicy", "hoppy"]
ipa = ["piney", "hoppy", "resin"]
lambic = ["tart", "fruity", "sour"]
mead = ["honey", "semi-sweet"]
oatmealStout = ["creamy", "roasted", "malty", "caramel"]
pilsner = ["sweet", "malty", "caramel", "spice"]
porter = ["roasted", "malty", "chocolate"]
saison = ["creamy", "malty", "citrus", "tart"]
schwarzbier = ["bittersweet", "malty"]
scotchAle = ["caramel", "toffee", "roasted", "malty"]
stout = ["roasted", "malty", "caramel", "hoppy"

#create CSV of the flavors array
import CSV
with open(flavors.csv", "w", newline="") as file:
    write = csv.writer(file)
    writer.writerows(flavors)

