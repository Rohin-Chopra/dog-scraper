import { ChildNode } from "domhandler";

export const getFirstChildData = (
  childNode: ChildNode | Element | undefined
): string => {
  if (childNode && "children" in childNode && "data" in childNode.firstChild!)
    return childNode.firstChild.data;

  return "";
};
