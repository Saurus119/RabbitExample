import React, { Component } from 'react';
import CosmonauntApi from '../api/CosmonauntApi.tsx';

class DemoComponent extends Component {
    state = {
        data: null,
        loading: true,
        error: null
    };

    Api = new CosmonauntApi()

    async componentDidMount() {
        var response = await this.Api.GetCosmonaunts(5);
        console.log("Mounting hook" + response);
    }

    render() {
        const {data} = this.state;

        return (
            <div>
              {/* Render your component using the fetched data */}
              {data && <p>Data: {data}</p>}
              <p>Jsem testovaci data</p>
            </div>
          );
    }
}

export default DemoComponent