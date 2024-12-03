export function parseJSON(inputJSON) {
    try {
      const data = JSON.parse(inputJSON);
      if (!data.coefficients || !data.init || !data.step || !data.dot) {
        throw new Error("Некорректный формат данных!");
      }
      return data;
    } catch (error) {
      console.error("Ошибка парсинга JSON:", error);
      throw error;
    }
  }
  