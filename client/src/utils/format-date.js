const formatDate = (datetime) => {
  const options = {
    year: "numeric",
    month: "long",
    day: "numeric",
    hour: "numeric",
    minute: "numeric",
  };
  return new Date(datetime).toLocaleString(undefined, options);
};

export default formatDate;
