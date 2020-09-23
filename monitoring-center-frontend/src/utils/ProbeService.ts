import Probe from '@/models/probe';
import axios, { AxiosInstance } from 'axios';

export default class ProbeService {
  private http: AxiosInstance

  constructor(serverBaseUrl: string) {
    this.http = axios.create({
      baseURL: serverBaseUrl,
      headers: {
        'Content-type': 'application/json',
      },
    });
  }

  async getAllProbes(): Promise<Probe[]> {
    const result = await this.http.get('/probes');
    return result.data;
  }
}
