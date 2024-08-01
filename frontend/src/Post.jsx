import React, { useEffect, useState } from 'react';
import { HeaderPost } from './components/Header';
import Comment from './Comment';
import apiFetch from './services/api-fetch';
import './static/stylesPost.css';

const Post = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    apiFetch("posts")
      .then((res) => {
        setData(res);
        setLoading(false);
      });
  }, []);

  console.log(data);
  if (loading) return <p>Cargando Posts...</p>;

  return (
    <div className="post-content">
      <HeaderPost />
      <div className="post-container">
        {data.map((d) => (
          <div className="post-wrapper" key={d.id}>
            <div className="post">
              <p>{d.content}</p>
            </div>
            <div className="comment">
              <Comment post_id={d.id}/>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Post;
