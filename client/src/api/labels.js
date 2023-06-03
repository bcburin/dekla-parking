import api, { baseRootUrl, createBaseAPI } from "src/api/api";

const baseLabelUrl = `${baseRootUrl}/labels`;

const labelsAPI = {
  ...createBaseAPI("labels"),
};

export default labelsAPI;
