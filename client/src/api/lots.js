import api, { baseRootUrl, createBaseAPI } from "src/api/api";

const baseLotUrl = `${baseRootUrl}/lots`;

const lotsAPI = {
  ...createBaseAPI("lots"),
  getUnassignedLots: async () => {
    const response = await api.get(
      `${baseLotUrl}/?skip=0&limit=100&unassigned=true`
    );
    return response.data;
  },
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
  bookForMe: async (lotId, bookTimes) => {
    const response = await api.post(
      `${baseLotUrl}/${lotId}/book-for-me`,
      bookTimes
    );
    return response.data;
  },
};

export default lotsAPI;
