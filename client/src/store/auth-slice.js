import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  isAuthenticated: false,
  isLoading: true,
  token: null,
};

const authSlice = createSlice({
  name: "auth",
  initialState,
  reducers: {
    initialize: (state, action) => {
      const token = action.payload;
      if (token) {
        state.isAuthenticated = true;
        state.isLoading = false;
        state.token = token;
      } else {
        state.isAuthenticated = false;
        state.isLoading = false;
      }
    },
    signIn: (state, action) => {
      state.isAuthenticated = true;
      state.token = action.payload.token;
    },
    signOut: (state) => {
      state.isAuthenticated = false;
      state.token = false;
    },
  },
});

const { reducer, actions } = authSlice;

export const { initialize, signIn, signOut } = actions;

export default reducer;
