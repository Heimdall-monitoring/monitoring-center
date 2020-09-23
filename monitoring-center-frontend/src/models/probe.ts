export default class Probe {
    uuid: string;

    name: string;

    description: string;

    constructor(uuid: string, name: string, description: string) {
      this.uuid = uuid;
      this.name = name;
      this.description = description;
    }
}
