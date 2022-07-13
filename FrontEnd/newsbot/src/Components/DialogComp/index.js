import React from "react";
import { Typography, Box } from "@mui/material";


function DialogComp(props) {
    // props.renderr(Math.random());
  return (
    <Box>
      <Typography color="text.secondary" sx={{ mt: 2 }}>
        {props.title}
      </Typography>
      <Typography color="text.secondary" sx={{ mt: 2 }}>
        {props.description}
      </Typography>
      <Typography color="text.secondary" sx={{ mt: 2 }}>
        {props.date}
      </Typography>
    </Box>
  );
}

export default DialogComp;
