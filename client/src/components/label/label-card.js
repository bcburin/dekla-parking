import {
  Card,
  CardActions,
  CardContent,
  CardHeader,
  IconButton,
  Menu,
  MenuItem,
  Tooltip,
  Typography,
} from "@mui/material";
import React, { useEffect, useState } from "react";
import { Stack, SvgIcon, useTheme } from "@mui/material";

import ArrowCircleRightRoundedIcon from "@mui/icons-material/ArrowCircleRightRounded";
import DeleteRoundedIcon from "@mui/icons-material/DeleteRounded";
import EditRoundedIcon from "@mui/icons-material/EditRounded";
import InfoRoundedIcon from "@mui/icons-material/InfoRounded";
import MoreVertIcon from "@mui/icons-material/MoreVert";
import LabelIcon from "@mui/icons-material/Label";
import ConfirmationModal from "../confirmation-modal";
import labelsAPI from "src/api/labels";

const LabelCard = ({ receivedLabel, onUpdate }) => {
  const theme = useTheme();
  const [label, setLabel] = useState(receivedLabel);
  const [anchorEl, setAnchorEl] = useState(null);
  const [deleteLabelModalIsOpen, setDeleteLabelModalIsOpen] = useState(false);
  let closeTimeout;

  const handleDeleteLabel = async () => {
    try {
      await labelsAPI.deleteEntity(label.id);
      if (onUpdate) await onUpdate();
    } catch (e) {
      console.log(e);
    }
  };

  const getColor = () => "#" + label?.color || theme.palette.primary.main;

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

  console.log(label);

  return (
    label && (
      <>
        <Card sx={{ maxWidth: 300 }}>
          <CardHeader
            avatar={
              <SvgIcon
                sx={{
                  color: getColor(),
                  fontSize: theme.typography.pxToRem(42),
                }}
              >
                <LabelIcon />
              </SvgIcon>
            }
            action={
              <IconButton aria-label="options" onClick={handleMenuOpen}>
                <MoreVertIcon />
              </IconButton>
            }
            title={label.name}
          ></CardHeader>
          <CardContent
            sx={{
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              flexDirection: "column",
              padding: theme.spacing(3),
              backgroundColor: theme.palette.common.white,
            }}
          >
            <Stack spacing={2} alignItems="center">
              {label.description && (
                <Typography
                  variant="body2"
                  sx={{
                    color: theme.palette.text.secondary,
                    textAlign: "left",
                    overflow: "hidden",
                    textOverflow: "ellipsis",
                    display: "-webkit-box",
                    WebkitLineClamp: 2,
                    WebkitBoxOrient: "vertical",
                  }}
                >
                  {label.description}
                </Typography>
              )}
            </Stack>
          </CardContent>
          <CardActions>
            <Tooltip title="Information">
              <IconButton aria-label="view" onClick={() => {}}>
                <InfoRoundedIcon />
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
              onClick={() => setDeleteLabelModalIsOpen(true)}
            >
              <DeleteRoundedIcon />
            </IconButton>
          </MenuItem>
          <MenuItem title="Assign to User">
            <IconButton aria-label="assign" onClick={() => {}}>
              <ArrowCircleRightRoundedIcon />
            </IconButton>
          </MenuItem>
          <MenuItem title="Edit">
            <IconButton aria-label="edit" onClick={() => {}}>
              <EditRoundedIcon />
            </IconButton>
          </MenuItem>
        </Menu>
        {label && (
          <ConfirmationModal
            open={deleteLabelModalIsOpen}
            onClose={() => setDeleteLabelModalIsOpen(false)}
            onConfirm={handleDeleteLabel}
            title="Delete Label"
            content={`Are you sure you want to delete label "${label.name}"`}
          />
        )}
      </>
    )
  );
};

export default LabelCard;
