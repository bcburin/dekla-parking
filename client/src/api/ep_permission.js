import api, { baseRootUrl, createBaseAPI } from "./api";


const epPermissionAPI = {
  ...createBaseAPI("epPermissions"),
};

export default epPermissionAPI;
