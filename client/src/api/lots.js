import api, { baseRootUrl, createBaseAPI } from "src/api/api";

const baseLotUrl = `${baseRootUrl}/lots`;

const lotsAPI = {
  ...createBaseAPI("lots"),
  toggleOccupied: async (lotId) => {
    const response = await api.put(`${baseLotUrl}/${lotId}/toggle-occupied`);
    return response.data;
  },
  toggleActive: async (lotId) => {
    const response = await api.put(`${baseLotUrl}/${lotId}/toggle-active`);
    return response.data;
  },
  assign: async (lotId, sectorId) => {
    const response = await api.put(`${baseLotUrl}/${lotId}/assign/${sectorId}`);
    return response.data;
  },
};

export default lotsAPI;
