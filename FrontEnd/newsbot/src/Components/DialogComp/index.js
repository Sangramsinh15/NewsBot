import React from "react";
import { Typography, Box, Grid, Link } from "@mui/material";

function DialogComp(props) {
  // props.renderr(Math.random());
  return (
    <Grid sx={{borderBottom:1}}>
      <Box
        component="div"
        sx={{
          display: "inline",
          fontSize: 16,
          fontFamily: "Arial",
          fontWeight: "bold",
        }}
      >
        ({props.ind}) Title: {props.title}
      </Box>
      <Box
        component="div"
        sx={{
          pt: 1,
          pl: 3,
          fontSize: 16,
          fontFamily: "Arial",
          fontWeight: "bold",
        }}
      >
        Desc: {props.description}
      </Box>

      <Box
        component="div"
        sx={{
          display: "inline",
          pt: 1,
          pl: 3,
          fontSize: 16,
          fontFamily: "Arial",
          fontWeight: "bold",
        }}
      >
        Link:
      </Box>

      <Link
        href={props.link}
        sx={{
          pt: 1,
          pl: 3,
          fontSize: 16,
          fontFamily: "Arial",
          fontWeight: "bold",
        }}
      >
        Link
      </Link>
      <Grid container>
        <Box sx={{ flexGrow: 1 }}></Box>
        <Box
          component="span"
          sx={{
            pr:3,
            fontSize: 12,
            fontFamily: "Arial",
            fontWeight: "bold",
          }}
        >
          Date: {props.date}
        </Box>
      </Grid>
    </Grid>
  );
}

export default DialogComp;
