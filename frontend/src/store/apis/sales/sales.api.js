
import {rootApi} from "../root.api.js";

export const salesAllGetApi = async () => {
    try {
        const response = await rootApi.get("/sales/")
        return response.data 
    } catch (error) {
        return error

    }


}