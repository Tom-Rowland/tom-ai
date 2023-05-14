import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faGithub } from '@fortawesome/free-brands-svg-icons';
import './TopBar.css'

const TopBar = () => {
    return (
        <div className="top-bar">
            <div className="app-name">tom.ai</div>
            <div className="buttons">
                <a href="https://github.com/Tom-Rowland/tom-ai" target="_blank" rel="noopener noreferrer">
                    <FontAwesomeIcon icon ={faGithub} />
                </a>
            </div>
        </div>
    );
};

export default TopBar;