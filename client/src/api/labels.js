import api, { baseRootUrl, createBaseAPI } from "src/api/api";

const baseLabelUrl = `${baseRootUrl}/labels`;

const labelsAPI = {
  ...createBaseAPI("labels"),
  assignToUser: async (labelId, userId, labelingTimes) => {
    const response = await api.post(
      `${baseLabelUrl}/${labelId}/assign-to/${userId}`,
      labelingTimes
    );
    return response.data;
  },
};

export default labelsAPI;
