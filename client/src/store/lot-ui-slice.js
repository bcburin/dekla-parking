import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  selectedLot: null,
  showLotModalIsOpen: false,
  deleteLotModalIsOpen: false,
  assignLotModalIsOpen: false,
  editLotModalIsOpen: false,
  bookLotModalIsOpen: false,
};

const lotUISlice = createSlice({
  name: "lotUI",
  initialState,
  reducers: {
    openShowLotModal: (state, action) => {
      state.selectedLot = action.payload.lot;
      state.showLotModalIsOpen = true;
    },
    openDeleteLotModal: (state, action) => {
      state.selectedLot = action.payload.lot;
      state.deleteLotModalIsOpen = true;
    },
    openAssignLotModal: (state, action) => {
      state.selectedLot = action.payload.lot;
      state.assignLotModalIsOpen = true;
    },
    openEditLotModal: (state, action) => {
      state.selectedLot = action.payload.lot;
      state.editLotModalIsOpen = true;
    },
    openBookLotModal: (state, action) => {
      state.selectedLot = action.payload.lot;
      state.bookLotModalIsOpen = true;
    },
    closeShowLotModal: (state) => {
      state.selectedLot = null;
      state.showLotModalIsOpen = false;
    },
    closeDeleteLotModal: (state) => {
      state.selectedLot = null;
      state.deleteLotModalIsOpen = false;
    },
    closeAssignLotModal: (state) => {
      state.selectedLot = null;
      state.assignLotModalIsOpen = false;
    },
    closeEditLotModal: (state) => {
      state.selectedLot = null;
      state.editLotModalIsOpen = false;
    },
    closeBookLotModal: (state) => {
      state.selectedLot = null;
      state.bookLotModalIsOpen = false;
    },
  },
});

export const { reducer, actions } = lotUISlice;

export default reducer;
