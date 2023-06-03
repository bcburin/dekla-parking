import {
  Avatar,
  Card,
  CardActions,
  CardContent,
  CardHeader,
  IconButton,
  Menu,
  MenuItem,
  Tooltip,
} from "@mui/material";
import React, { useEffect, useState } from "react";
import { Stack, SvgIcon, useTheme } from "@mui/material";

import ArrowCircleRightRoundedIcon from "@mui/icons-material/ArrowCircleRightRounded";
import BookmarksRoundedIcon from "@mui/icons-material/BookmarksRounded";
import DeleteRoundedIcon from "@mui/icons-material/DeleteRounded";
import DirectionsCarFilledRoundedIcon from "@mui/icons-material/DirectionsCarFilledRounded";
import EditRoundedIcon from "@mui/icons-material/EditRounded";
import InfoRoundedIcon from "@mui/icons-material/InfoRounded";
import MoreVertIcon from "@mui/icons-material/MoreVert";
import ToggleOffRoundedIcon from "@mui/icons-material/ToggleOnRounded";
import ToggleOnRoundedIcon from "@mui/icons-material/ToggleOnRounded";
import { actions } from "src/store/lot-ui-slice";
import lotsAPI from "src/api/lots";
import { useDispatch } from "react-redux";

const LotCard = ({ receivedLot }) => {
  const dispatch = useDispatch();
  const theme = useTheme();
  const [lot, setLot] = useState(receivedLot);
  const [anchorEl, setAnchorEl] = useState(null);
  let closeTimeout;

  const getColor = () => {
    return lot.occupied ? theme.palette.error.dark : theme.palette.success.dark;
  };

  const toggleLotOccupiedHandler = async () => {
    try {
      const lot = await lotsAPI.toggleOccupied(receivedLot.id);
      setLot(lot);
    } catch (e) {
      console.log(e);
    }
  };

  const handleMenuOpen = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleMenuClose = () => {
    closeTimeout = setTimeout(() => {
      setAnchorEl(null);
    }, 100);
  };

  useEffect(() => {
    return () => {
      clearTimeout(closeTimeout); // Cleanup the timeout on component unmount
    };
  }, []);

  return (
    <>
      <Card sx={{ maxWidth: 300 }}>
        <CardHeader
          avatar={
            <Avatar sx={{ bgcolor: getColor() }}>
              {lot.location.substring(0, 2)}
            </Avatar>
          }
          action={
            <IconButton aria-label="options" onClick={handleMenuOpen}>
              <MoreVertIcon />
            </IconButton>
          }
          title={lot.name}
          subheader={lot.id}
        ></CardHeader>
        <CardContent
          sx={{
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            flexDirection: "column",
            padding: theme.spacing(3),
            backgroundColor: theme.palette.common.white,
            color: getColor(),
          }}
        >
          <Stack spacing={2} alignItems="center">
            <SvgIcon
              sx={{
                fontSize: theme.typography.pxToRem(72),
              }}
            >
              <DirectionsCarFilledRoundedIcon />
            </SvgIcon>
          </Stack>
        </CardContent>
        <CardActions>
          <Tooltip title="Information">
            <IconButton
              aria-label="view"
              onClick={() => dispatch(actions.openShowLotModal({ lot }))}
            >
              <InfoRoundedIcon />
            </IconButton>
          </Tooltip>
          <Tooltip title="Book Parking Lot">
            <IconButton
              aria-label="book-lot"
              onClick={() => dispatch(actions.openBookLotModal({ lot }))}
            >
              <BookmarksRoundedIcon />
            </IconButton>
          </Tooltip>
          <Tooltip title="Toggle Occupied">
            <IconButton
              aria-label="toggle-occupied"
              onClick={toggleLotOccupiedHandler}
            >
              {lot.occupied ? (
                <ToggleOffRoundedIcon />
              ) : (
                <ToggleOnRoundedIcon />
              )}
            </IconButton>
          </Tooltip>
        </CardActions>
      </Card>
      <Menu
        anchorEl={anchorEl}
        open={Boolean(anchorEl)}
        onClose={handleMenuClose}
        MenuListProps={{
          onMouseLeave: handleMenuClose,
          onMouseOver: () => {
            clearTimeout(closeTimeout);
          },
        }}
      >
        <MenuItem title="Delete">
          <IconButton
            aria-label="delete"
            onClick={() => dispatch(actions.openDeleteLotModal({ lot }))}
          >
            <DeleteRoundedIcon />
          </IconButton>
        </MenuItem>
        <MenuItem title="Assign to Sector">
          <IconButton
            aria-label="assign"
            onClick={() => dispatch(actions.openAssignLotModal({ lot }))}
          >
            <ArrowCircleRightRoundedIcon />
          </IconButton>
        </MenuItem>
        <MenuItem title="Edit">
          <IconButton
            aria-label="edit"
            onClick={() => dispatch(actions.openEditLotModal({ lot }))}
          >
            <EditRoundedIcon />
          </IconButton>
        </MenuItem>
      </Menu>
    </>
  );
};

export default LotCard;
