import axios, { AxiosInstance } from 'axios';

export default class ApiBase {
    baseUrl: string;
    customAxios: AxiosInstance

  constructor() {
    this.customAxios = axios.create({})
    this.customAxios.defaults.baseURL = "http://127.0.0.1:8000"
  }

  public async Get(endpoint: string, params: object) {
    const url = endpoint;
    console.log("Sending data to the url:" + this.customAxios.getUri());
    try {
      const response = await this.customAxios.get(endpoint, { params });
      return this.JsonifyResponse(response.data);
    } catch (error) {
      throw this.handleRequestError(error);
    }
  }

  public async Post(endpoint: string, data: object) {
    const url = this.constructUrl(endpoint);
    try {
      const response = await axios.post(url, data);
      return response.data;
    } catch (error) {
      throw this.handleRequestError(error);
    }
  }

  public async Delete(endpoint: string, id: any) {
    const url = this.constructUrl(endpoint);
    try {
      const response = await axios.delete(url);
      return response.data;
    } catch (error) {
      throw this.handleRequestError(error);
    }
  }

  public async Patch(endpoint: string, data: object) {
    const url = this.constructUrl(endpoint);
    try {
      const response = await axios.patch(url, data);
      return response.data;
    } catch (error) {
      throw this.handleRequestError(error);
    }
  }

  private JsonifyResponse(response) {
    try {
        return JSON.parse(response.data)
    } catch (error) {
        this.handleRequestError(error);
    }
  }

  private constructUrl(endpoint: string) {
    return `${this.baseUrl}/${endpoint}`;
  }

  private handleRequestError(error) {
    // Handle and customize error handling as needed
    console.error('Request Error:', error);
    throw error;
  }
}
