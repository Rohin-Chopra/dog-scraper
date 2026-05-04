export enum State {
  VIC = "VIC",
  QLD = "QLD",
  NSW = "NSW",
  ACT = "ACT",
  TAS = "TAS",
  SA = "SA",
  WA = "WA",
  NT = "NT",
  NZ = "NZ",
  AUST_AND_NZ = "AUST & NZ",
}

export interface Listing {
  breederName: string;
  phone: string;
  location: string;
  lastUpdatedOn: Date;
}

export interface CreateCheerioOptions {
  state: State;
  breed: string;
}
