import { Button } from "@mui/material";
import React from "react";
import { Box } from "@mui/material";

function GenreComp(props) {
  const [open, setOpen] = React.useState(false);
  const handleOpen = () => setOpen(true);

  const handleClick =  (e) => {
    var data = JSON.stringify({
        text: props.text,
        session_id: "1234",
      });
  
      var config = {
        method: "post",
        url: "http://44.200.109.25:80/get_response_2",
        headers: {
          "Content-Type": "application/json",
        },
        data: data,
      };
  
      await axios(config)
        .then(function(response) {
          console.log(JSON.stringify(response));
          const api2Response = response.data.message;
        })
        .catch(function(error) {
          console.log(error);
        });
      setResult(tempResult);
      setTags(mytags);
      console.log(tags);
      setOpen(true)
    };
  

  return (
    <Box sx={{ pt: 0.2, pr: 0.2 }}>
      <Button onClick={handleOpen} variant="contained">
        {props.text}
      </Button>
      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={style}>
          <Typography
            id="modal-modal-title"
            variant="h5"
            component="h2"
            sx={{ mb: 2 }}
          >
            Articles Related to {props.text}:
          </Typography>
          <Divider />
          <Typography sx={{ mt: 2 }}>
            {props.desc}
          </Typography>
          <Typography sx={{ mt: 2 }}>
            {props.desc}
          </Typography>
        </Box>
      </Modal>
    </Box>
  );
}

export default GenreComp;
