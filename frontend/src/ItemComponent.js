import React from 'react';

export default function ItemComponent(props){
    const status = props.status;
    return <li>Item desc.: { props.name }, Status: {status ? <p>Finalizado</p> : <p>Não Finalizado</p>}</li>   
}