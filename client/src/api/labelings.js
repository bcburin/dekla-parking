import api, { baseRootUrl, createBaseAPI } from "./api";


const LabelingsAPI = {
  ...createBaseAPI("labelings"),
};

export default LabelingsAPI;
