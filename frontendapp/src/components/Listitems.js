import React from 'react'
import {Link} from 'react-router-dom'



let trimmedTitle = (note) => {
  let content = note.body
  if(content.length > 45){
    return content.slice(0,45)+ '...'
  }
  else return content
}

let getTimestamp = (note) => {
  return new Date(note.__updatedtime__).toLocaleDateString()
}




const Listitems = ({note}) => {
  return (
    <Link to={`/${note.id}`}>
      <div className='notes-list-item'>
        <h3>{trimmedTitle(note)}</h3>
        <p><span>{getTimestamp(note)}</span></p>
      </div> 
    </Link>
  )
}

export default Listitems;