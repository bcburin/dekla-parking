import api, { baseRootUrl, createBaseAPI } from "./api";

const publicPolicyAPI = {
  ...createBaseAPI("public_policies"),
};

export default publicPolicyAPI;
