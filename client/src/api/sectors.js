import api, { baseRootUrl, createBaseAPI } from "src/api/api";

const baseSectorsUrl = `${baseRootUrl}/sectors`;

const sectorAPI = {
  ...createBaseAPI("sectors"),
  assignPublicPolicy: async (sectorId, policyId) => {
    const response = await api.put(
      `${baseSectorsUrl}/${sectorId}/assign-public-policy/${policyId}`
    );
    return response.data;
  },
  assignExclusivePolicy: async (sectorId, policyId) => {
    const response = await api.put(
      `${baseSectorsUrl}/${sectorId}/assign-exclusive-policy/${policyId}`
    );
    return response.data;
  },
};

export default sectorAPI;
