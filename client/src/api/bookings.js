import api, { baseRootUrl, createBaseAPI } from "./api";

const baseBookingUrl = `${baseRootUrl}/bookings`;

const bookingsAPI = {
  ...createBaseAPI("bookings"),
  approve: async (bookingId) => {
    const response = await api.put(`${baseBookingUrl}/${bookingId}/approve`);
    return response.data;
  },
  reject: async (bookingId) => {
    const response = await api.put(`${baseBookingUrl}/${bookingId}/reject`);
    return response.data;
  },
};

export default bookingsAPI;
