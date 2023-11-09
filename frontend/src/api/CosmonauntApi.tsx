import ApiBase from "./_base/ApiBase.tsx"

export default class CosmonauntApi extends ApiBase {
    Route: string = "/cosmonaunt"

    constructor() {
        super()
    }

    public async GetCosmonaunts(limit?: number, order?: number) {
        var response = await this.Get(this.Route, {})
        return response;
    }

}