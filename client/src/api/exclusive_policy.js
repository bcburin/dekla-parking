import api, { baseRootUrl, createBaseAPI } from "./api";


const exclusivePolicyAPI = {
  ...createBaseAPI("exclusive_policies"),
};

export default exclusivePolicyAPI;
