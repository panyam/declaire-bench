package dev.declairebench.inventory;

import dev.declairebench.inventory.v1.GetItemRequest;
import dev.declairebench.inventory.v1.GetItemResponse;
import dev.declairebench.inventory.v1.InventoryServiceGrpc;
import dev.declairebench.inventory.v1.Item;
import dev.declairebench.inventory.v1.ReserveItemRequest;
import dev.declairebench.inventory.v1.ReserveItemResponse;
import io.grpc.Status;
import io.grpc.stub.StreamObserver;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.atomic.AtomicLong;

/** Serves InventoryService from stock held in memory. */
public class InventoryServiceImpl extends InventoryServiceGrpc.InventoryServiceImplBase {
  private final Map<String, Item> items = new HashMap<>();
  private final AtomicLong nextReservation = new AtomicLong(1);

  public InventoryServiceImpl(Iterable<Item> stock) {
    for (Item item : stock) {
      items.put(item.getSku(), item);
    }
  }

  @Override
  public void getItem(GetItemRequest request, StreamObserver<GetItemResponse> responses) {
    Item item = items.get(request.getSku());
    if (item == null) {
      responses.onError(Status.NOT_FOUND.withDescription(request.getSku()).asRuntimeException());
      return;
    }
    responses.onNext(GetItemResponse.newBuilder().setItem(item).build());
    responses.onCompleted();
  }

  @Override
  public synchronized void reserveItem(
      ReserveItemRequest request, StreamObserver<ReserveItemResponse> responses) {
    Item item = items.get(request.getSku());
    if (item == null) {
      responses.onError(Status.NOT_FOUND.withDescription(request.getSku()).asRuntimeException());
      return;
    }
    if (request.getQuantity() <= 0 || request.getQuantity() > item.getOnHand()) {
      responses.onError(
          Status.FAILED_PRECONDITION
              .withDescription("only " + item.getOnHand() + " on hand")
              .asRuntimeException());
      return;
    }
    int remaining = item.getOnHand() - request.getQuantity();
    items.put(item.getSku(), item.toBuilder().setOnHand(remaining).build());
    responses.onNext(
        ReserveItemResponse.newBuilder()
            .setReservationId(request.getOrderId() + "-" + nextReservation.getAndIncrement())
            .setRemaining(remaining)
            .build());
    responses.onCompleted();
  }
}
