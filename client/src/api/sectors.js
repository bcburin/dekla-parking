import api, { createBaseAPI } from "src/api/api";

const sectorAPI = {
  ...createBaseAPI("sectors"),
};

export default sectorAPI;
