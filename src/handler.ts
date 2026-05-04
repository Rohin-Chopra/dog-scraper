import { CheerioAPI, load } from "cheerio";
import dayjs from "dayjs";
import { CreateCheerioOptions, Listing, State } from "./types";
import { getFirstChildData } from "./utils";

const createCheerioByStateAndBreed = async ({
  state,
  breed,
}: CreateCheerioOptions): Promise<CheerioAPI> => {
  const url = new URL(
    `https://www.dogzonline.com.au/breeds/puppies/${breed}.asp`
  );
  if (state !== State.AUST_AND_NZ) url.searchParams.set("state", state);

  const response = await fetch(url.toString());

  return load(await response.text());
};

const getListings = (cheerio: CheerioAPI): Listing[] => {
  return cheerio("#main > div.row > div.col-xs-12.eqdiv > article > div > dl")
    .map((index, element): Listing => {
      return {
        breederName: getFirstChildData(element.children[3]),
        location: getFirstChildData(element.children[7]),
        phone: getFirstChildData(element.children[11]),
        lastUpdatedOn: new Date(
          getFirstChildData(
            cheerio("#main > div.row > div.col-xs-12.eqdiv span.plan").get(
              index
            )
          ).replace("Last Updated : ", "")
        ),
      };
    })
    .toArray();
};

const filterByLatestListings = (
  listings: Listing[],
  daysInterval = 2
): Listing[] => {
  return listings.filter((listing) => {
    const today = dayjs();

    return today.diff(listing.lastUpdatedOn, "day") <= daysInterval;
  });
};

const main = async () => {
  const cheerio = await createCheerioByStateAndBreed({
    state: State.VIC,
    breed: "german-shepherd-dog",
  });

  const latestListings = filterByLatestListings(getListings(cheerio));

  console.log(latestListings);
};

(async () => {
  await main();
})();
