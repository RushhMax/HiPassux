import React, { useEffect, useState } from 'react';
import apiFetch from './services/api-fetch';
import PropTypes from 'prop-types';

const Comment = ({ post_id }) => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    apiFetch("comments")
      .then((res) => {
        setData(res);
        setLoading(false);
      });
  }, []);

  console.log(data);
  if (loading) return <p>Cargando Posts...</p>;

  return (
    <>
        {data.filter((d) => d.post_id == post_id).map((d) => (
          <div className="post-wrapper" key={d.id}>
            <div className="post">
              <p>{d.content}</p>
              {/* <p>{d.user_id}</p> */}
            </div>
          </div>
        ))}
    </>
  );
};

Comment.prototype = {
  post_id: PropTypes.string.isRequired,
}

export default Comment;
